{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "45a77219",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Tính đóng gói\n",
    "class Smartphone:\n",
    "    def __init__(self, name, price, chipset):\n",
    "        self.name = name\n",
    "        self.price = price\n",
    "        self.chipset = chipset\n",
    "    def sell(self):\n",
    "        return self.name + ',' + self.price + ',' + self.chipset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "8e71bd13",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Xiaomi note pro,1200,888'"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Tính kế thừa\n",
    "class Customer(Smartphone):\n",
    "    def __init__(self, name, price, chipset):\n",
    "        super(). __init__(name, price, chipset)\n",
    "\n",
    "Hieu = Customer('Xiaomi note pro', '1200', '888')\n",
    "Hieu.sell()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "d573638c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Gâu Gâu\n",
      "Meo Meo\n"
     ]
    }
   ],
   "source": [
    "#Tính đa hình\n",
    "class Animal:\n",
    "    def Suadi(self):\n",
    "        print(\"Sủa đi nào\")\n",
    "\n",
    "class Chó(Animal):\n",
    "    def Suadi(self):\n",
    "        print(\"Gâu Gâu\")\n",
    "\n",
    "class Mèo(Animal):\n",
    "    def Suadi(self):\n",
    "        print(\"Meo Meo\")\n",
    "\n",
    "chó = Chó()\n",
    "chó.Suadi()\n",
    "\n",
    "mèo = Mèo()\n",
    "mèo.Suadi()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "7420bef2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nguyen Trong Hieu\n",
      "19\n"
     ]
    }
   ],
   "source": [
    "#tính trừu tượng\n",
    "from abc import ABC, abstractmethod\n",
    "\n",
    "class PersonAbstact(ABC):\n",
    "    name = None\n",
    "    age = 0\n",
    "    def Name(self):\n",
    "        print(self.name)\n",
    "    def Age(self):\n",
    "        print(self.age)\n",
    "    def Me(self):\n",
    "        pass\n",
    "\n",
    "class Person(PersonAbstact):\n",
    "    name = 'Nguyen Trong Hieu'\n",
    "    age = 19\n",
    "    def Me(self):\n",
    "        self.Name()\n",
    "        self.Age()\n",
    "\n",
    "Person().Me()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25b90f88",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
