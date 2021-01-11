---
title: JViewport.setUI()
permalink: Java/JViewport/setUI
date: 2021-01-11
key: JavaJava.J.JViewport
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JViewport.metodos valor="setUI" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(hidden=true, visualUpdate=true, description="The UI object that implements the Component\'s LookAndFeel.") public void setUI(ViewportUI ui)
~~~

## Parámetros
* **ViewportUI ui**,  {% include w3api/param_description.html metodo=_dato parametro="ViewportUI ui" %}

## Clase Padre
[JViewport](/Java/JViewport/)

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
