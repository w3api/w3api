---
title: RepaintManager.getVolatileOffscreenBuffer()
permalink: /Java/RepaintManager/getVolatileOffscreenBuffer/
date: 2021-01-11
key: Java.R.RepaintManager
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RepaintManager.metodos valor="getVolatileOffscreenBuffer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Image getVolatileOffscreenBuffer(Component c, int proposedWidth, int proposedHeight)
~~~

## Parámetros
* **int proposedWidth**,  {% include w3api/param_description.html metodo=_dato parametro="int proposedWidth" %}
* **int proposedHeight**,  {% include w3api/param_description.html metodo=_dato parametro="int proposedHeight" %}
* **Component c**,  {% include w3api/param_description.html metodo=_dato parametro="Component c" %}

## Clase Padre
[RepaintManager](/Java/RepaintManager/)

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
