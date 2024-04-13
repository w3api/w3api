---
title: InputStream.transferTo()
permalink: /Java/InputStream-java-io/transferTo/
date: 2021-01-11
key: Java.I.InputStream-java-io
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputStream-java-io.metodos valor="transferTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long transferTo(OutputStream out) throws IOException
~~~

## Parámetros
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[InputStream](/Java/InputStream-java-io/)

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
