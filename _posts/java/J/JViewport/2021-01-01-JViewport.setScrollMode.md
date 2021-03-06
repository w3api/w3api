---
title: JViewport.setScrollMode()
permalink: /Java/JViewport/setScrollMode/
date: 2021-01-11
key: Java.J.JViewport
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JViewport.metodos valor="setScrollMode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, enumerationValues={"JViewport.BLIT_SCROLL_MODE","JViewport.BACKINGSTORE_SCROLL_MODE","JViewport.SIMPLE_SCROLL_MODE"}, description="Method of moving contents for incremental scrolls.") public void setScrollMode(int mode)
~~~

## Parámetros
* **int mode**,  {% include w3api/param_description.html metodo=_dato parametro="int mode" %}

## Clase Padre
[JViewport](/Java/JViewport/)

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
