---
title: BasicLookAndFeel.loadSystemColors()
permalink: /Java/BasicLookAndFeel/loadSystemColors/
date: 2021-01-11
key: Java.B.BasicLookAndFeel
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicLookAndFeel.metodos valor="loadSystemColors" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void loadSystemColors(UIDefaults table, String[] systemColors, boolean useNative)
~~~

## Parámetros
* **String[] systemColors**,  {% include w3api/param_description.html metodo=_dato parametro="String[] systemColors" %}
* **boolean useNative**,  {% include w3api/param_description.html metodo=_dato parametro="boolean useNative" %}
* **UIDefaults table**,  {% include w3api/param_description.html metodo=_dato parametro="UIDefaults table" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BasicLookAndFeel](/Java/BasicLookAndFeel/)

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
