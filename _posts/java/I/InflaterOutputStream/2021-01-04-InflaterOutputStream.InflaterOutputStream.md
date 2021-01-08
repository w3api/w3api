---
title: InflaterOutputStream.InflaterOutputStream()
permalink: Java/InflaterOutputStream/InflaterOutputStream
date: 2021-01-04
key: JavaJava.I.InflaterOutputStream
category: java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InflaterOutputStream.constructores valor="InflaterOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InflaterOutputStream(OutputStream out)
public InflaterOutputStream(OutputStream out, Inflater infl)
public InflaterOutputStream(OutputStream out, Inflater infl, int bufLen)
~~~

## Parámetros
* **int bufLen**,  {% include w3api/param_description.html metodo=_data parametro="int bufLen" %}
* **Inflater infl**,  {% include w3api/param_description.html metodo=_data parametro="Inflater infl" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[InflaterOutputStream](/Java/InflaterOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InflaterOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
