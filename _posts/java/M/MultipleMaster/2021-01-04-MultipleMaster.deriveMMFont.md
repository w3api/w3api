---
title: MultipleMaster.deriveMMFont()
permalink: Java/MultipleMaster/deriveMMFont
date: 2021-01-04
key: JavaJava.M.MultipleMaster
category: java
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
* **float[] axes**,  {% include w3api/param_description.html metodo=_data parametro="float[] axes" %}
* **float italicAngle**,  {% include w3api/param_description.html metodo=_data parametro="float italicAngle" %}
* **float[] glyphWidths**,  {% include w3api/param_description.html metodo=_data parametro="float[] glyphWidths" %}
* **float typicalXHeight**,  {% include w3api/param_description.html metodo=_data parametro="float typicalXHeight" %}
* **float typicalCapHeight**,  {% include w3api/param_description.html metodo=_data parametro="float typicalCapHeight" %}
* **float avgStemWidth**,  {% include w3api/param_description.html metodo=_data parametro="float avgStemWidth" %}

## Clase Padre
[MultipleMaster](/Java/MultipleMaster/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MultipleMaster.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
