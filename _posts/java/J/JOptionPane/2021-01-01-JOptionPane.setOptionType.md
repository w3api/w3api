---
title: JOptionPane.setOptionType()
permalink: /Java/JOptionPane/setOptionType/
date: 2021-01-11
key: Java.J.JOptionPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JOptionPane.metodos valor="setOptionType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, description="The option pane\'s option type.") public void setOptionType(int newType)
~~~

## Parámetros
* **int newType**,  {% include w3api/param_description.html metodo=_dato parametro="int newType" %}

## Excepciones
[RuntimeException](/Java/RuntimeException/)

## Clase Padre
[JOptionPane](/Java/JOptionPane/)

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
