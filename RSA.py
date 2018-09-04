#RSA

def generate_keys(p,q):
    def xgcd(b, a):
        n = (a)
        x0, x1, y0, y1 = 1, 0, 0, 1
        while a != 0:
            q, b, a = b // a, a, b % a
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        if b == 1:
            return x0 % n
    
    import math,random
    n = p * q

    etn = (p-1)*(q-1)

    primes = []
    for i in range(3,etn):
        prime = True
        for j in range(2,math.ceil(i**0.5)):
            if not i % j:
                prime = False
                break
        if prime:
            primes.append(i)
    #e = (random.choice(primes),n)
    e = 7
    d = xgcd (e,etn)
    return ((e,n),(d,n))

def encrypt(message, p,n):
    return (message ** p) % n

def decrypt(c, q, n):
    o =  c**q
    print("1")
    o = o % n
    print("2")
    return o

if False:
    public_key, private_key = keygen(11,13)
    print(public_key,private_key)
    print(encrypt(15, public_key))
    print(decrypt(115,private_key))

if True:
    c = 95272795986475189505518980251137003509292621140166383887854853863720692420204142448424074834657149326853553097626486371206617513769930277580823116437975487148956107509247564965652417450550680181691869432067892028368985007229633943149091684419834136214793476910417359537696632874045272326665036717324623992885
    p = 11387480584909854985125335848240384226653929942757756384489381242206157197986555243995335158328781970310603060671486688856263776452654268043936036556215243
    q = 12972222875218086547425818961477257915105515705982283726851833508079600460542479267972050216838604649742870515200462359007315431848784163790312424462439629
    n = p * q
    print("n")
    print(decrypt(c,q,n))
