---
title: JTabbedPane.setTabLayoutPolicy()
permalink: /Java/JTabbedPane/setTabLayoutPolicy/
date: 2021-01-11
key: Java.J.JTabbedPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.metodos valor="setTabLayoutPolicy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, visualUpdate=true, enumerationValues={"JTabbedPane.WRAP_TAB_LAYOUT","JTabbedPane.SCROLL_TAB_LAYOUT"}, description="The tabbedpane\'s policy for laying out the tabs") public void setTabLayoutPolicy(int tabLayoutPolicy)
~~~

## Parámetros
* **int tabLayoutPolicy**,  {% include w3api/param_description.html metodo=_dato parametro="int tabLayoutPolicy" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JTabbedPane](/Java/JTabbedPane/)

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
