---
title: CheckedOutputStream.CheckedOutputStream()
permalink: Java/CheckedOutputStream/CheckedOutputStream
date: 2021-01-04
key: JavaJava.C.CheckedOutputStream
category: java
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
* **Checksum cksum**,  {% include w3api/param_description.html metodo=_data parametro="Checksum cksum" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}

## Clase Padre
[CheckedOutputStream](/Java/CheckedOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CheckedOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
