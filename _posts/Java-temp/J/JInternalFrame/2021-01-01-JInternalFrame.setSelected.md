---
title: JInternalFrame.setSelected()
permalink: /Java/JInternalFrame/setSelected/
date: 2021-01-11
key: Java.J.JInternalFrame
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JInternalFrame.metodos valor="setSelected" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(description="Indicates whether this internal frame is currently the active frame.") public void setSelected(boolean selected) throws PropertyVetoException
~~~

## Parámetros
* **boolean selected**,  {% include w3api/param_description.html metodo=_dato parametro="boolean selected" %}

## Excepciones
[PropertyVetoException](/Java/PropertyVetoException/)

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
