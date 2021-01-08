---
title: JTabbedPane.setUI()
permalink: Java/JTabbedPane/setUI
date: 2021-01-04
key: JavaJava.J.JTabbedPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.metodos valor="setUI" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(hidden=true, visualUpdate=true, description="The UI object that implements the tabbedpane\'s LookAndFeel") public void setUI(TabbedPaneUI ui)
~~~

## Parámetros
* **TabbedPaneUI ui**,  {% include w3api/param_description.html metodo=_data parametro="TabbedPaneUI ui" %}

## Clase Padre
[JTabbedPane](/Java/JTabbedPane/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JTabbedPane.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
