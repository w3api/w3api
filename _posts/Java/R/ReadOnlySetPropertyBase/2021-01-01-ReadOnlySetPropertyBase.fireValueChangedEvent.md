---
title: ReadOnlySetPropertyBase.fireValueChangedEvent()
permalink: /Java/ReadOnlySetPropertyBase/fireValueChangedEvent/
date: 2021-01-11
key: Java.R.ReadOnlySetPropertyBase
category: Java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ReadOnlySetPropertyBase.metodos valor="fireValueChangedEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void fireValueChangedEvent()
protected void fireValueChangedEvent(SetChangeListener.Change<? extends E> change)
~~~

## Parámetros
* **SetChangeListener.Change&lt;? extends E&gt; change**,  {% include w3api/param_description.html metodo=_dato parametro="SetChangeListener.Change<? extends E> change" %}

## Clase Padre
[ReadOnlySetPropertyBase](/Java/ReadOnlySetPropertyBase/)

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
