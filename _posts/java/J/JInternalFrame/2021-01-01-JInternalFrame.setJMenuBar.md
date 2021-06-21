---
title: JInternalFrame.setJMenuBar()
permalink: /Java/JInternalFrame/setJMenuBar/
date: 2021-01-11
key: Java.J.JInternalFrame
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JInternalFrame.metodos valor="setJMenuBar" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, description="The menu bar for accessing pulldown menus from this internal frame.") public void setJMenuBar(JMenuBar m)
~~~

## Parámetros
* **JMenuBar m**,  {% include w3api/param_description.html metodo=_dato parametro="JMenuBar m" %}

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
