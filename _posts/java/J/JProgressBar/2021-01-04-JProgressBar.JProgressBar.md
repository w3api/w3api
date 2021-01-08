---
title: JProgressBar.JProgressBar()
permalink: Java/JProgressBar/JProgressBar
date: 2021-01-04
key: JavaJava.J.JProgressBar
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JProgressBar.constructores valor="JProgressBar" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JProgressBar()
public JProgressBar(int orient)
public JProgressBar(int min, int max)
public JProgressBar(int orient, int min, int max)
public JProgressBar(BoundedRangeModel newModel)
~~~

## Parámetros
* **int min**,  {% include w3api/param_description.html metodo=_data parametro="int min" %}
* **int max**,  {% include w3api/param_description.html metodo=_data parametro="int max" %}
* **BoundedRangeModel newModel**,  {% include w3api/param_description.html metodo=_data parametro="BoundedRangeModel newModel" %}
* **int orient**,  {% include w3api/param_description.html metodo=_data parametro="int orient" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JProgressBar](/Java/JProgressBar/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JProgressBar.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
