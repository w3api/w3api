---
title: AbstractButton.setVerticalAlignment()
permalink: Java/AbstractButton/setVerticalAlignment
date: 2021-01-10
key: JavaJava.A.AbstractButton
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractButton.metodos valor="setVerticalAlignment" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(visualUpdate=true, enumerationValues={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"}, description="The vertical alignment of the icon and text.") public void setVerticalAlignment(int alignment)
~~~

## Parámetros
* **int alignment**,  {% include w3api/param_description.html metodo=_dato parametro="int alignment" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
