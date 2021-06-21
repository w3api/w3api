---
title: JInternalFrame.JInternalFrame()
permalink: /Java/JInternalFrame/JInternalFrame/
date: 2021-01-11
key: Java.J.JInternalFrame
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JInternalFrame.constructores valor="JInternalFrame" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JInternalFrame()
public JInternalFrame(String title)
public JInternalFrame(String title, boolean resizable)
public JInternalFrame(String title, boolean resizable, boolean closable)
public JInternalFrame(String title, boolean resizable, boolean closable, boolean maximizable)
public JInternalFrame(String title, boolean resizable, boolean closable, boolean maximizable, boolean iconifiable)
~~~

## Parámetros
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **boolean resizable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean resizable" %}
* **boolean maximizable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean maximizable" %}
* **boolean iconifiable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean iconifiable" %}
* **boolean closable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean closable" %}

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
