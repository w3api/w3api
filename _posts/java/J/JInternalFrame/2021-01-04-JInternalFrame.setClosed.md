---
title: JInternalFrame.setClosed()
permalink: Java/JInternalFrame/setClosed
date: 2021-01-04
key: JavaJava.J.JInternalFrame
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JInternalFrame.metodos valor="setClosed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(description="Indicates whether this internal frame has been closed.") public void setClosed(boolean b) throws PropertyVetoException
~~~

## Parámetros
* **boolean b**,  {% include w3api/param_description.html metodo=_data parametro="boolean b" %}

## Excepciones
[PropertyVetoException](/Java/PropertyVetoException/)

## Clase Padre
[JInternalFrame](/Java/JInternalFrame/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JInternalFrame.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
