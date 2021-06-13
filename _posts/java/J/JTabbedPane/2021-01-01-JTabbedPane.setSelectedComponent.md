---
title: JTabbedPane.setSelectedComponent()
permalink: /Java/JTabbedPane/setSelectedComponent/
date: 2021-01-11
key: Java.J.JTabbedPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.metodos valor="setSelectedComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, preferred=true, description="The tabbedpane\'s selected component.") public void setSelectedComponent(Component c)
~~~

## Parámetros
* **Component c**,  {% include w3api/param_description.html metodo=_dato parametro="Component c" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JTabbedPane](/Java/JTabbedPane/)

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
