---
title: ImageReadParam.setSourceProgressivePasses()
permalink: /Java/ImageReadParam/setSourceProgressivePasses/
date: 2021-01-11
key: Java.I.ImageReadParam
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReadParam.metodos valor="setSourceProgressivePasses" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSourceProgressivePasses(int minPass, int numPasses)
~~~

## Parámetros
* **int minPass**,  {% include w3api/param_description.html metodo=_dato parametro="int minPass" %}
* **int numPasses**,  {% include w3api/param_description.html metodo=_dato parametro="int numPasses" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageReadParam](/Java/ImageReadParam/)

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
