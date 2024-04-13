---
title: GapContent.replace()
permalink: /Java/GapContent/replace/
date: 2021-01-11
key: Java.G.GapContent
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GapContent.metodos valor="replace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void replace(int position, int rmSize, Object addItems, int addSize)
~~~

## Parámetros
* **int position**,  {% include w3api/param_description.html metodo=_dato parametro="int position" %}
* **int rmSize**,  {% include w3api/param_description.html metodo=_dato parametro="int rmSize" %}
* **int addSize**,  {% include w3api/param_description.html metodo=_dato parametro="int addSize" %}
* **Object addItems**,  {% include w3api/param_description.html metodo=_dato parametro="Object addItems" %}

## Clase Padre
[GapContent](/Java/GapContent/)

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
