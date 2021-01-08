---
title: CipherSpi.engineInit()
permalink: Java/CipherSpi/engineInit
date: 2021-01-04
key: JavaJava.C.CipherSpi
category: java
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
* **int opmode**,  {% include w3api/param_description.html metodo=_data parametro="int opmode" %}
* **AlgorithmParameterSpec params**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameterSpec params" %}
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_data parametro="SecureRandom random" %}
* **AlgorithmParameters params**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameters params" %}
* **Key key**,  {% include w3api/param_description.html metodo=_data parametro="Key key" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[CipherSpi](/Java/CipherSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CipherSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
