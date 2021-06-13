---
title: JFileChooser.setDialogType()
permalink: /Java/JFileChooser/setDialogType/
date: 2021-01-11
key: Java.J.JFileChooser
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JFileChooser.metodos valor="setDialogType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, enumerationValues={"JFileChooser.OPEN_DIALOG","JFileChooser.SAVE_DIALOG","JFileChooser.CUSTOM_DIALOG"}, description="The type (open, save, custom) of the JFileChooser.") public void setDialogType(int dialogType)
~~~

## Parámetros
* **int dialogType**,  {% include w3api/param_description.html metodo=_dato parametro="int dialogType" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JFileChooser](/Java/JFileChooser/)

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
