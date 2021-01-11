---
title: SignatureSpi.engineInitVerify()
permalink: Java/SignatureSpi/engineInitVerify
date: 2021-01-11
key: JavaJava.S.SignatureSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SignatureSpi.metodos valor="engineInitVerify" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineInitVerify(PublicKey publicKey) throws InvalidKeyException
~~~

## Parámetros
* **PublicKey publicKey**,  {% include w3api/param_description.html metodo=_dato parametro="PublicKey publicKey" %}

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
