---
title: JOptionPane.createDialog()
permalink: /Java/JOptionPane/createDialog/
date: 2021-01-11
key: Java.J.JOptionPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JOptionPane.metodos valor="createDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JDialog createDialog(Component parentComponent, String title) throws HeadlessException
public JDialog createDialog(String title) throws HeadlessException
~~~

## Parámetros
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **Component parentComponent**,  {% include w3api/param_description.html metodo=_dato parametro="Component parentComponent" %}

## Excepciones
[HeadlessException](/Java/HeadlessException/)

## Clase Padre
[JOptionPane](/Java/JOptionPane/)

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
