---
title: CheckedOutputStream.CheckedOutputStream()
permalink: /Java/CheckedOutputStream/CheckedOutputStream/
date: 2021-01-11
key: Java.C.CheckedOutputStream
category: Java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CheckedOutputStream.constructores valor="CheckedOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CheckedOutputStream(OutputStream out, Checksum cksum)
~~~

## Parámetros
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}
* **Checksum cksum**,  {% include w3api/param_description.html metodo=_dato parametro="Checksum cksum" %}

## Clase Padre
[CheckedOutputStream](/Java/CheckedOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
