---
title: CipherSpi.engineInit()
permalink: /Java/CipherSpi/engineInit/
date: 2021-01-11
key: Java.C.CipherSpi
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CipherSpi.metodos valor="engineInit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineInit(int opmode, Key key, AlgorithmParameters params, SecureRandom random) throws InvalidKeyException, InvalidAlgorithmParameterException
protected abstract void engineInit(int opmode, Key key, SecureRandom random) throws InvalidKeyException
protected abstract void engineInit(int opmode, Key key, AlgorithmParameterSpec params, SecureRandom random) throws InvalidKeyException, InvalidAlgorithmParameterException
~~~

## Parámetros
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameterSpec params" %}
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandom random" %}
* **Key key**,  {% include w3api/param_description.html metodo=_dato parametro="Key key" %}
* **int opmode**,  {% include w3api/param_description.html metodo=_dato parametro="int opmode" %}
* **AlgorithmParameters params**,  {% include w3api/param_description.html metodo=_dato parametro="AlgorithmParameters params" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[CipherSpi](/Java/CipherSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
