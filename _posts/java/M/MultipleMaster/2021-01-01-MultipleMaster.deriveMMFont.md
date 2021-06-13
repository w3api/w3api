---
title: MultipleMaster.deriveMMFont()
permalink: /Java/MultipleMaster/deriveMMFont/
date: 2021-01-11
key: Java.M.MultipleMaster
category: Java
tags: ['java se', 'java.awt.font', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MultipleMaster.metodos valor="deriveMMFont" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Font deriveMMFont(float[] axes)
Font deriveMMFont(float[] glyphWidths, float avgStemWidth, float typicalCapHeight, float typicalXHeight, float italicAngle)
~~~

## Parámetros
* **float avgStemWidth**,  {% include w3api/param_description.html metodo=_dato parametro="float avgStemWidth" %}
* **float[] glyphWidths**,  {% include w3api/param_description.html metodo=_dato parametro="float[] glyphWidths" %}
* **float typicalCapHeight**,  {% include w3api/param_description.html metodo=_dato parametro="float typicalCapHeight" %}
* **float[] axes**,  {% include w3api/param_description.html metodo=_dato parametro="float[] axes" %}
* **float typicalXHeight**,  {% include w3api/param_description.html metodo=_dato parametro="float typicalXHeight" %}
* **float italicAngle**,  {% include w3api/param_description.html metodo=_dato parametro="float italicAngle" %}

## Clase Padre
[MultipleMaster](/Java/MultipleMaster/)

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
