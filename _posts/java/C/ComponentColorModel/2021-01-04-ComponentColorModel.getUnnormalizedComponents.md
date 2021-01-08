---
title: ComponentColorModel.getUnnormalizedComponents()
permalink: Java/ComponentColorModel/getUnnormalizedComponents
date: 2021-01-04
key: JavaJava.C.ComponentColorModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComponentColorModel.metodos valor="getUnnormalizedComponents" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int[] getUnnormalizedComponents(float[] normComponents, int normOffset, int[] components, int offset)
~~~

## Parámetros
* **int normOffset**,  {% include w3api/param_description.html metodo=_data parametro="int normOffset" %}
* **float[] normComponents**,  {% include w3api/param_description.html metodo=_data parametro="float[] normComponents" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **int[] components**,  {% include w3api/param_description.html metodo=_data parametro="int[] components" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ComponentColorModel](/Java/ComponentColorModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ComponentColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
