---
title: JComponent.setTransferHandler()
permalink: /Java/JComponent/setTransferHandler/
date: 2021-01-11
key: Java.J.JComponent
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComponent.metodos valor="setTransferHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(hidden=true, description="Mechanism for transfer of data to and from the component") public void setTransferHandler(TransferHandler newHandler)
~~~

## Parámetros
* **TransferHandler newHandler**,  {% include w3api/param_description.html metodo=_dato parametro="TransferHandler newHandler" %}

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
