---
title: SignatureSpi.engineUpdate()
permalink: Java/SignatureSpi/engineUpdate
date: 2021-01-04
key: JavaJava.S.SignatureSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SignatureSpi.metodos valor="engineUpdate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineUpdate(byte b) throws SignatureException
protected abstract void engineUpdate(byte[] b, int off, int len) throws SignatureException
protected void engineUpdate(ByteBuffer input)
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **ByteBuffer input**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer input" %}
* **byte[] b**,  {% include w3api/param_description.html metodo=_data parametro="byte[] b" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **byte b**,  {% include w3api/param_description.html metodo=_data parametro="byte b" %}

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
