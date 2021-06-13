---
title: JInternalFrame.setLayeredPane()
permalink: /Java/JInternalFrame/setLayeredPane/
date: 2021-01-11
key: Java.J.JInternalFrame
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JInternalFrame.metodos valor="setLayeredPane" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(hidden=true, description="The pane which holds the various desktop layers.") public void setLayeredPane(JLayeredPane layered)
~~~

## Parámetros
* **JLayeredPane layered**,  {% include w3api/param_description.html metodo=_dato parametro="JLayeredPane layered" %}

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
