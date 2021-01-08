---
title: JProgressBar.setModel()
permalink: Java/JProgressBar/setModel
date: 2021-01-04
key: JavaJava.J.JProgressBar
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JProgressBar.metodos valor="setModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, expert=true, description="The data model used by the JProgressBar.") public void setModel(BoundedRangeModel newModel)
~~~

## Parámetros
* **BoundedRangeModel newModel**,  {% include w3api/param_description.html metodo=_data parametro="BoundedRangeModel newModel" %}

## Clase Padre
[JProgressBar](/Java/JProgressBar/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JProgressBar.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
