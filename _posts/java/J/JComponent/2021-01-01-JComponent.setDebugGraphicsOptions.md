---
title: JComponent.setDebugGraphicsOptions()
permalink: /Java/JComponent/setDebugGraphicsOptions/
date: 2021-01-11
key: Java.J.JComponent
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComponent.metodos valor="setDebugGraphicsOptions" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, preferred=true, enumerationValues={"DebugGraphics.NONE_OPTION","DebugGraphics.LOG_OPTION","DebugGraphics.FLASH_OPTION","DebugGraphics.BUFFERED_OPTION"}, description="Diagnostic options for graphics operations.") public void setDebugGraphicsOptions(int debugOptions)
~~~

## Parámetros
* **int debugOptions**,  {% include w3api/param_description.html metodo=_dato parametro="int debugOptions" %}

## Clase Padre
[JComponent](/Java/JComponent/)

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
