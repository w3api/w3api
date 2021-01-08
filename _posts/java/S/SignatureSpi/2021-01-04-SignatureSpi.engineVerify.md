---
title: SignatureSpi.engineVerify()
permalink: Java/SignatureSpi/engineVerify
date: 2021-01-04
key: JavaJava.S.SignatureSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SignatureSpi.metodos valor="engineVerify" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract boolean engineVerify(byte[] sigBytes) throws SignatureException
protected boolean engineVerify(byte[] sigBytes, int offset, int length) throws SignatureException
~~~

## Parámetros
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **byte[] sigBytes**,  {% include w3api/param_description.html metodo=_data parametro="byte[] sigBytes" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[SignatureException](/Java/SignatureException/)

## Clase Padre
[SignatureSpi](/Java/SignatureSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SignatureSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
