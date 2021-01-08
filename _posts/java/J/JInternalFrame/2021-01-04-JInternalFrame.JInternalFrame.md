---
title: JInternalFrame.JInternalFrame()
permalink: Java/JInternalFrame/JInternalFrame
date: 2021-01-04
key: JavaJava.J.JInternalFrame
category: java
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
* **String title**,  {% include w3api/param_description.html metodo=_data parametro="String title" %}
* **boolean closable**,  {% include w3api/param_description.html metodo=_data parametro="boolean closable" %}
* **boolean resizable**,  {% include w3api/param_description.html metodo=_data parametro="boolean resizable" %}
* **boolean maximizable**,  {% include w3api/param_description.html metodo=_data parametro="boolean maximizable" %}
* **boolean iconifiable**,  {% include w3api/param_description.html metodo=_data parametro="boolean iconifiable" %}

## Clase Padre
[JInternalFrame](/Java/JInternalFrame/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JInternalFrame.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
