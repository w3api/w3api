---
title: JInternalFrame.remove()
permalink: /Java/JInternalFrame/remove/
date: 2021-01-11
key: Java.J.JInternalFrame
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JInternalFrame.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void remove(Component comp)
~~~

## Parámetros
* **Component comp**,  {% include w3api/param_description.html metodo=_dato parametro="Component comp" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[JInternalFrame](/Java/JInternalFrame/)

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
