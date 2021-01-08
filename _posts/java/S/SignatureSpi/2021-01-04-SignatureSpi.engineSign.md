---
title: SignatureSpi.engineSign()
permalink: Java/SignatureSpi/engineSign
date: 2021-01-04
key: JavaJava.S.SignatureSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SignatureSpi.metodos valor="engineSign" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract byte[] engineSign() throws SignatureException
protected int engineSign(byte[] outbuf, int offset, int len) throws SignatureException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **byte[] outbuf**,  {% include w3api/param_description.html metodo=_data parametro="byte[] outbuf" %}
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
