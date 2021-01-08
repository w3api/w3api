---
title: CheckedInputStream.CheckedInputStream()
permalink: Java/CheckedInputStream/CheckedInputStream
date: 2021-01-04
key: JavaJava.C.CheckedInputStream
category: java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CheckedInputStream.constructores valor="CheckedInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CheckedInputStream(InputStream in, Checksum cksum)
~~~

## Parámetros
* **Checksum cksum**,  {% include w3api/param_description.html metodo=_data parametro="Checksum cksum" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_data parametro="InputStream in" %}

## Clase Padre
[CheckedInputStream](/Java/CheckedInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CheckedInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
