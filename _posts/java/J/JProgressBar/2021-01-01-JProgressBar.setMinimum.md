---
title: JProgressBar.setMinimum()
permalink: /Java/JProgressBar/setMinimum/
date: 2021-01-11
key: Java.J.JProgressBar
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JProgressBar.metodos valor="setMinimum" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, preferred=true, description="The progress bar\'s minimum value.") public void setMinimum(int n)
~~~

## Parámetros
* **int n**,  {% include w3api/param_description.html metodo=_dato parametro="int n" %}

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
