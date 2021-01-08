---
title: SampleModel.getSampleSize()
permalink: Java/SampleModel/getSampleSize
date: 2021-01-04
key: JavaJava.S.SampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SampleModel.metodos valor="getSampleSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int[] getSampleSize()
public abstract int getSampleSize(int band)
~~~

## Parámetros
* **int band**,  {% include w3api/param_description.html metodo=_data parametro="int band" %}

## Clase Padre
[SampleModel](/Java/SampleModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SampleModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
