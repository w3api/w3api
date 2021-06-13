---
title: SignatureSpi.engineSign()
permalink: /Java/SignatureSpi/engineSign/
date: 2021-01-11
key: Java.S.SignatureSpi
category: Java
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
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **byte[] outbuf**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] outbuf" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
