---
title: AbstractButton.setHorizontalAlignment()
permalink: Java/AbstractButton/setHorizontalAlignment
date: 2021-01-04
key: JavaJava.A.AbstractButton
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractButton.metodos valor="setHorizontalAlignment" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(visualUpdate=true, enumerationValues={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"}, description="The horizontal alignment of the icon and text.") public void setHorizontalAlignment(int alignment)
~~~

## Parámetros
* **int alignment**,  {% include w3api/param_description.html metodo=_data parametro="int alignment" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AbstractButton](/Java/AbstractButton/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractButton.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
