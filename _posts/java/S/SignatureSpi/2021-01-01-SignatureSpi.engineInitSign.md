---
title: SignatureSpi.engineInitSign()
permalink: Java/SignatureSpi/engineInitSign
date: 2021-01-11
key: JavaJava.S.SignatureSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SignatureSpi.metodos valor="engineInitSign" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineInitSign(PrivateKey privateKey) throws InvalidKeyException
protected void engineInitSign(PrivateKey privateKey, SecureRandom random) throws InvalidKeyException
~~~

## Parámetros
* **PrivateKey privateKey**,  {% include w3api/param_description.html metodo=_dato parametro="PrivateKey privateKey" %}
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandom random" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/)

## Clase Padre
[SignatureSpi](/Java/SignatureSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
