---
title: DeflaterInputStream.DeflaterInputStream()
permalink: Java/DeflaterInputStream/DeflaterInputStream
date: 2021-01-04
key: JavaJava.D.DeflaterInputStream
category: java
tags: ['java se', 'java.util.zip', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DeflaterInputStream.constructores valor="DeflaterInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DeflaterInputStream(InputStream in)
public DeflaterInputStream(InputStream in, Deflater defl)
public DeflaterInputStream(InputStream in, Deflater defl, int bufLen)
~~~

## Parámetros
* **int bufLen**,  {% include w3api/param_description.html metodo=_data parametro="int bufLen" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_data parametro="InputStream in" %}
* **Deflater defl**,  {% include w3api/param_description.html metodo=_data parametro="Deflater defl" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DeflaterInputStream](/Java/DeflaterInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DeflaterInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
