---
title: SynthStyle.getColorForState()
permalink: /Java/SynthStyle/getColorForState/
date: 2021-01-11
key: Java.S.SynthStyle
category: Java
tags: ['java se', 'javax.swing.plaf.synth', 'java.desktop', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SynthStyle.metodos valor="getColorForState" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract Color getColorForState(SynthContext context, ColorType type)
~~~

## Parámetros
* **SynthContext context**,  {% include w3api/param_description.html metodo=_dato parametro="SynthContext context" %}
* **ColorType type**,  {% include w3api/param_description.html metodo=_dato parametro="ColorType type" %}

## Clase Padre
[SynthStyle](/Java/SynthStyle/)

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
