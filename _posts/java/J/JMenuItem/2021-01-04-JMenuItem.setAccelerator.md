---
title: JMenuItem.setAccelerator()
permalink: Java/JMenuItem/setAccelerator
date: 2021-01-04
key: JavaJava.J.JMenuItem
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMenuItem.metodos valor="setAccelerator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, description="The keystroke combination which will invoke the JMenuItem\'s actionlisteners without navigating the menu hierarchy") public void setAccelerator(KeyStroke keyStroke)
~~~

## Parámetros
* **KeyStroke keyStroke**,  {% include w3api/param_description.html metodo=_data parametro="KeyStroke keyStroke" %}

## Clase Padre
[JMenuItem](/Java/JMenuItem/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JMenuItem.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
