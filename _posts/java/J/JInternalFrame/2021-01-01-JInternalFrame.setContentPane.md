---
title: JInternalFrame.setContentPane()
permalink: /Java/JInternalFrame/setContentPane/
date: 2021-01-11
key: Java.J.JInternalFrame
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JInternalFrame.metodos valor="setContentPane" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(hidden=true, description="The client area of the internal frame where child components are normally inserted.") public void setContentPane(Container c)
~~~

## Parámetros
* **Container c**,  {% include w3api/param_description.html metodo=_dato parametro="Container c" %}

## Excepciones
[IllegalComponentStateException](/Java/IllegalComponentStateException/)

## Clase Padre
[JInternalFrame](/Java/JInternalFrame/)

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
