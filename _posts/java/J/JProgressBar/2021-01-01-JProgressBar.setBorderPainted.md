---
title: JProgressBar.setBorderPainted()
permalink: /Java/JProgressBar/setBorderPainted/
date: 2021-01-11
key: Java.J.JProgressBar
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JProgressBar.metodos valor="setBorderPainted" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(visualUpdate=true, description="Whether the progress bar should paint its border.") public void setBorderPainted(boolean b)
~~~

## Parámetros
* **boolean b**,  {% include w3api/param_description.html metodo=_dato parametro="boolean b" %}

## Clase Padre
[JProgressBar](/Java/JProgressBar/)

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
