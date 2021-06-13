---
title: JProgressBar.setOrientation()
permalink: /Java/JProgressBar/setOrientation/
date: 2021-01-11
key: Java.J.JProgressBar
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JProgressBar.metodos valor="setOrientation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, visualUpdate=true, description="Set the progress bar\'s orientation.") public void setOrientation(int newOrientation)
~~~

## Parámetros
* **int newOrientation**,  {% include w3api/param_description.html metodo=_dato parametro="int newOrientation" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
