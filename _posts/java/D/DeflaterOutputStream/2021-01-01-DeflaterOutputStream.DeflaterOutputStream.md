---
title: DeflaterOutputStream.DeflaterOutputStream()
permalink: Java/DeflaterOutputStream/DeflaterOutputStream
date: 2021-01-11
key: JavaJava.D.DeflaterOutputStream
category: java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DeflaterOutputStream.constructores valor="DeflaterOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DeflaterOutputStream(OutputStream out)
public DeflaterOutputStream(OutputStream out, boolean syncFlush)
public DeflaterOutputStream(OutputStream out, Deflater def)
public DeflaterOutputStream(OutputStream out, Deflater def, boolean syncFlush)
public DeflaterOutputStream(OutputStream out, Deflater def, int size)
public DeflaterOutputStream(OutputStream out, Deflater def, int size, boolean syncFlush)
~~~

## Parámetros
* **Deflater def**,  {% include w3api/param_description.html metodo=_dato parametro="Deflater def" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}
* **int size**,  {% include w3api/param_description.html metodo=_dato parametro="int size" %}
* **boolean syncFlush**,  {% include w3api/param_description.html metodo=_dato parametro="boolean syncFlush" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DeflaterOutputStream](/Java/DeflaterOutputStream/)

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
